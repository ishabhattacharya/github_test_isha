from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        s3.Bucket(
                self,
                "MyBucket",
                versioned=True)

