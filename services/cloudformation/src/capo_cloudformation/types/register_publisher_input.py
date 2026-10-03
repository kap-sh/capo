"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegisterPublisherInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.accept_terms_and_conditions
    import capo_cloudformation.types.connection_arn


class RegisterPublisherInput(TypedDict, closed=True):
    accept_terms_and_conditions: NotRequired[
        "capo_cloudformation.types.accept_terms_and_conditions.AcceptTermsAndConditions"
    ]
    """<p>Whether you accept the <a href="https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf">Terms and Conditions</a> for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.</p> <p>The default is <code>false</code>.</p>"""
    connection_arn: NotRequired[
        "capo_cloudformation.types.connection_arn.ConnectionArn"
    ]
    """<p>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Prerequisite: Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterPublisherInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "accept_terms_and_conditions" in value:
        pairs.append(
            (
                f"{key_prefix}AcceptTermsAndConditions",
                "true" if value["accept_terms_and_conditions"] else "false",
            )
        )
    if "connection_arn" in value:
        pairs.append((f"{key_prefix}ConnectionArn", str(value["connection_arn"])))


def deserialize_query(el: Element) -> RegisterPublisherInput:
    out: RegisterPublisherInput = {}  # type: ignore[typeddict-item]
    child_accept_terms_and_conditions = el.find("AcceptTermsAndConditions")
    if child_accept_terms_and_conditions is not None:
        out["accept_terms_and_conditions"] = (
            child_accept_terms_and_conditions.text or ""
        ).lower() == "true"
    child_connection_arn = el.find("ConnectionArn")
    if child_connection_arn is not None:
        out["connection_arn"] = str(child_connection_arn.text or "")
    return out
