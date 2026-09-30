import aws_cdk as cdk

from worknow_infra.stack import WorkNowStack

REGION = "eu-central-1"

app = cdk.App()
# No account is set: this skeleton is synth-only and must not be deployed.
WorkNowStack(app, "WorkNowStack", env=cdk.Environment(region=REGION))
app.synth()
