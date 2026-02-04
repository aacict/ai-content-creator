output "lambda_function_name" {
  value = aws_lambda_function.ai_poster.function_name
}

output "lambda_arn" {
  value = aws_lambda_function.ai_poster.arn
}

output "eventbridge_rule" {
  value = aws_cloudwatch_event_rule.daily_trigger.name
}
