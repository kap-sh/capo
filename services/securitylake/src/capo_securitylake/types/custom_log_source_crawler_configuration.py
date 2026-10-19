"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceCrawlerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.role_arn


class CustomLogSourceCrawlerConfiguration(TypedDict, closed=True):
    role_arn: "capo_securitylake.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be used by the Glue crawler. The recommended IAM policies are:</p> <ul> <li> <p>The managed policy <code>AWSGlueServiceRole</code> </p> </li> <li> <p>A custom policy granting access to your Amazon S3 Data Lake</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceCrawlerConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CustomLogSourceCrawlerConfiguration:
    out: CustomLogSourceCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
