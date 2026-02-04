variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  type        = string
  default     = "ai-content-auto-poster"
}

variable "hf_token" {
  description = "Hugging Face API token"
  type        = string
  sensitive   = true
}

variable "fb_page_token" {
  description = "Facebook Page Access Token"
  type        = string
  sensitive   = true
}

variable "fb_page_id" {
  description = "Facebook Page ID"
  type        = string
}

variable "lambda_zip_path" {
  description = "Path to Lambda zip file"
  type        = string
  default     = "../lambda.zip"
}
