import aws_cdk as cdk
from aws_cdk.assertions import Template

from worknow_infra.stack import WorkNowStack


def test_stack_synthesizes_without_resources() -> None:
    app = cdk.App()
    stack = WorkNowStack(app, "TestStack", env=cdk.Environment(region="eu-central-1"))

    template = Template.from_stack(stack)

    assert template.to_json().get("Resources", {}) == {}
    assert stack.region == "eu-central-1"
