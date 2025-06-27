provider "aws" {
  region = "us-east-1"
  access_key = "SIMULADO"
  secret_key = "SIMULADO"
}

resource "aws_instance" "api_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}
