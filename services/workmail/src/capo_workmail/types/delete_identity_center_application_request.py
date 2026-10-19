"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteIdentityCenterApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.application_arn


class DeleteIdentityCenterApplicationRequest(TypedDict, closed=True):
    application_arn: "capo_workmail.types.application_arn.ApplicationArn"
    """<p> The Amazon Resource Name (ARN) of the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentityCenterApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentityCenterApplicationRequest:
    out: DeleteIdentityCenterApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    return out
