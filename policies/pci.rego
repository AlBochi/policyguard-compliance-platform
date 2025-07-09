package pci

# Example: Cardholder data must be encrypted in S3 buckets
deny[msg] {
    input.resource.type == "aws_s3_bucket"
    not input.resource.encryption.enabled
    msg := "PCI-DSS violation: Cardholder data must be encrypted in S3 buckets"
}

# Example: EC2 instances must have monitoring enabled
deny[msg] {
    input.resource.type == "aws_instance"
    input.resource.monitoring.enabled != true
    msg := "PCI-DSS violation: EC2 instance monitoring is not enabled"
}

