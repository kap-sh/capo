"""Generated from Smithy shape ``com.amazonaws.waf#CreateWebACLMigrationStackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.s3_object_url


class CreateWebACLMigrationStackResponse(TypedDict, closed=True):
    s3_object_url: "capo_waf.types.s3_object_url.S3ObjectUrl"
    """<p>The URL of the template created in Amazon S3. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLMigrationStackResponse) -> dict:
    out: dict = {}
    out["S3ObjectUrl"] = value["s3_object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLMigrationStackResponse:
    out: CreateWebACLMigrationStackResponse = {}  # type: ignore[typeddict-item]
    if data.get("S3ObjectUrl") is not None:
        out["s3_object_url"] = data["S3ObjectUrl"]
    else:
        out["s3_object_url"] = ""
    return out
