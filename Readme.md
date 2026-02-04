# AI Content Auto-Poster

Automated social media content generator that creates and posts AI-generated images with captions to Facebook using AWS Lambda and Hugging Face APIs.

## 🌟 Features

- **AI-Generated Content**: Uses Hugging Face models for text and image generation
- **Automated Posting**: Scheduled daily posts via AWS EventBridge
- **Serverless Architecture**: Runs entirely on AWS Lambda (no servers to manage)
- **Infrastructure as Code**: Complete Terraform configuration for easy deployment

## 🏗️ Architecture

```
EventBridge (Cron) → Lambda Function → Hugging Face API → Facebook Graph API
```

- **AWS Lambda**: Serverless function execution
- **AWS EventBridge**: Scheduled triggers (daily at 2 PM UTC)
- **Hugging Face API**:
  - Text generation (GLM-4.7-Flash)
  - Image generation (Stable Diffusion XL)
- **Facebook Graph API**: Posts content to your Facebook page

## 📋 Prerequisites

- AWS Account with CLI configured
- Hugging Face account and API token
- Facebook Page and API credentials
- Terraform installed
- Python 3.13
- PowerShell (for Windows) or Bash (for Linux/Mac)

## 🚀 Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-content-auto-poster
```

### 2. Get API Credentials

#### Hugging Face Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new token with `read` permissions
3. Copy the token

#### Facebook Page Token

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create an app and add Facebook Login product
3. Get a Page Access Token for your Facebook Page
4. Get your Page ID from your Facebook Page settings

### 3. Configure Terraform Variables

Create a `terraform.tfvars` file:

```hcl
lambda_function_name = "ai-content-auto-poster"
lambda_zip_path      = "lambda.zip"
hf_token             = "hf_your_token_here"
fb_page_token        = "your_facebook_page_token"
fb_page_id           = "your_facebook_page_id"
```

**⚠️ Important**: Add `terraform.tfvars` to `.gitignore` to protect your secrets!

### 4. Build the Lambda Package

**Windows (PowerShell):**

```powershell
.\build.ps1
```

**Linux/Mac (Bash):**

```bash
chmod +x deploy.sh
./deploy.sh
```

### 5. Deploy with Terraform

```bash
terraform init
terraform plan
terraform apply
```

Type `yes` when prompted to confirm deployment.

## 📁 Project Structure

```
.
├── lambda/
│   ├── main.py              # Main Lambda handler
│   ├── text_generator.py    # HF text generation
│   └── image_generator.py   # HF image generation
├── main.tf                  # Terraform infrastructure
├── variables.tf             # Terraform variables
├── outputs.tf               # Terraform outputs
├── requirements.txt         # Python dependencies
├── build.ps1               # Windows build script
├── build.sh                # Linux/Mac build script
└── README.md               # This file
```

## 🔧 Configuration

### Lambda Function Settings

- **Runtime**: Python 3.13
- **Memory**: 512 MB (adjustable in `main.tf`)
- **Timeout**: 300 seconds (5 minutes)
- **Schedule**: Daily at 2 PM UTC (configurable)

### Modify Schedule

Edit the cron expression in `main.tf`:

```hcl
resource "aws_cloudwatch_event_rule" "daily_trigger" {
  schedule_expression = "cron(0 14 * * ? *)"  # 2 PM UTC daily
}
```

Cron format: `cron(Minutes Hours Day-of-month Month Day-of-week Year)`

Examples:

- Every hour: `cron(0 * * * ? *)`
- Every day at 9 AM UTC: `cron(0 9 * * ? *)`
- Every Monday at 10 AM UTC: `cron(0 10 ? * MON *)`

## 🧪 Testing

### Test Lambda Function Locally

```python
# In lambda/main.py, add at the bottom:
if __name__ == "__main__":
    import os
    os.environ['HF_TOKEN'] = 'your_token'
    os.environ['FB_PAGE_TOKEN'] = 'your_token'
    os.environ['FB_PAGE_ID'] = 'your_page_id'

    lambda_handler({}, None)
```

Run:

```bash
cd lambda
python main.py
```

### Test in AWS Console

1. Go to AWS Lambda Console
2. Find your function
3. Click "Test" tab
4. Create a test event (empty `{}` is fine)
5. Click "Test"

## 📊 Monitoring

### View Logs

```bash
# Using AWS CLI
aws logs tail /aws/lambda/ai-content-auto-poster --follow
```

Or view in AWS Console:

1. CloudWatch → Log Groups
2. Find `/aws/lambda/ai-content-auto-poster`

### Check Metrics

- AWS Lambda Console → Your function → Monitor tab
- CloudWatch → Metrics → Lambda

## 🛠️ Troubleshooting

### Package Too Large Error

If you get "Request must be smaller than 70MB" error:

### zipped Size Too Large

If zipped size exceeds, you may need to:

1. Remove unnecessary dependencies
2. Use Lambda Layers
3. Switch to Container Image deployment

### API Errors

**Hugging Face API**:

- Check token validity
- Verify model availability
- Check API rate limits

**Facebook API**:

- Verify Page Access Token hasn't expired
- Check page permissions
- Ensure Page ID is correct

## 🔐 Security Best Practices

1. **Never commit secrets**: Keep `terraform.tfvars` in `.gitignore`
2. **Use AWS Secrets Manager**: For production, store secrets in AWS Secrets Manager
3. **Rotate tokens**: Regularly rotate API tokens
4. **Least privilege**: IAM role has minimal required permissions

## 💰 Cost Estimation

**AWS Costs (approximate):**

- Lambda: ~$0.20/month (1 execution/day)
- EventBridge: Free tier
- CloudWatch Logs: ~$0.50/month

**Total**: ~$1/month

**Hugging Face**: Free tier includes limited API calls

**Facebook**: Free

## 🔄 Updates & Maintenance

### Update Lambda Code

```bash
# Modify code in lambda/
.\build.ps1
terraform apply
```

### Update Dependencies

```bash
# Edit requirements.txt
# Rebuild package
.\build.ps1
terraform apply
```

### Destroy Infrastructure

```bash
terraform destroy
```

Type `yes` to confirm deletion of all resources.

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

- **Issues**: Open an issue on GitHub
- **AWS Documentation**: https://docs.aws.amazon.com/lambda/
- **Hugging Face Docs**: https://huggingface.co/docs
- **Terraform Docs**: https://registry.terraform.io/providers/hashicorp/aws/

## 🙏 Acknowledgments

- Hugging Face for API access
- AWS for serverless infrastructure
- Facebook for Graph API

---

**Happy Posting! 🚀**
