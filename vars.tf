variable "REGION" {
  default = "us-east-1"
}

variable "REGION_NEXUS" {
  default = "nexus"
}

variable "ZONE" {
  default = "us-east-1a"
}

variable "AMIS" {
  type = map(any)
  default = {
    # us-east-1 = "ami-06ca3ca175f37dd66"
    us-east-1 = "ami-06ca3ca175f37dd66"
    nexus     = "ami-002070d43b0a4f171"
  }
}

variable "JENKINS_SH" {
  default = "jenkins.sh"
}