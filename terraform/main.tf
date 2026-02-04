resource "aws_iam_role" "lambda_role" {
  name = "${var.lambda_function_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_lambda_function" "ai_poster" {
  function_name = var.lambda_function_name
  runtime       = "python3.13"
  handler       = "main.lambda_handler"

  filename         = var.lambda_zip_path
  source_code_hash = filebase64sha256(var.lambda_zip_path)

  role        = aws_iam_role.lambda_role.arn
  timeout     = 120
  memory_size = 1024

  environment {
    variables = {
      HF_TOKEN      = var.hf_token
      FB_PAGE_TOKEN = var.fb_page_token
      FB_PAGE_ID    = var.fb_page_id
    }
  }
}

resource "aws_cloudwatch_event_rule" "daily_trigger" {
  name                = "daily-ai-post"
  schedule_expression = "cron(0 14 * * ? *)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.daily_trigger.name
  target_id = "lambda"
  arn       = aws_lambda_function.ai_poster.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ai_poster.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_trigger.arn
}
