package soc2

# CC6.1: S3 buckets must have encryption enabled
deny[msg] {
  input.resource.type == "aws_s3_bucket"
  not input.resource.encryption.enabled
  msg := "SOC 2 CC6.1 violation: S3 encryption not enabled"
}

# CC7.1: EC2 instances must use approved AMIs
deny[msg] {
  input.resource.type == "aws_instance"
  not approved_ami(input.resource.ami)
  msg := "SOC 2 CC7.1 violation: Unapproved AMI"
}

approved_ami(ami) {
  ami == "ami-0abcdef1234567890"
}

approved_ami(ami) {
  ami == "ami-0fedcba9876543210"
}

