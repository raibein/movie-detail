resource "aws_instance" "ec2_jenkins_instance" {
  count                  = 1 # Create only one ec2 instance
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  availability_zone      = var.ZONE
  key_name               = "aws-devops-key"
  vpc_security_group_ids = ["sg-09505d3f7fcc6b5a4"]

  # Provide the tag names to make the search easy
  tags = {
    Name    = "jenkins_instance"
    Project = "jenkins"
  }

  # Establishes connection to be used by all
  connection {
    user        = "ec2-user"
    private_key = file("./cred/aws-devops-key.pem")
    host        = self.public_ip
  }

  # Copies the jenkins.sh file to /tmp/jenkins.sh
  provisioner "file" {
    source      = "./scripts/jenkins.sh"
    destination = "/tmp/jenkins_docker.sh"
  }

  # generic remote provisioners (i.e. file/remote-exec)
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/jenkins.sh",
      "sudo /tmp/jenkins.sh"
    ]
  }
}