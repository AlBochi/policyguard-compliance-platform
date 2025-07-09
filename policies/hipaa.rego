package hipaa

# PHI data in S3 must be encrypted
deny[msg] {
    input.resource.type == "aws_s3_bucket"
    contains(input.resource.name, "phi")
    not input.resource.encryption.enabled
    msg := "HIPAA violation: PHI data in S3 bucket must be encrypted"
}

# EC2 instances must have patching enabled
deny[msg] {
    input.resource.type == "aws_instance"
    input.resource.patching.enabled != true
    msg := "HIPAA violation: EC2 instance patching is not enabled"
}

