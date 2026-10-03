"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.snowflake_private_link_vpce_id


class SnowflakeVpcConfiguration(TypedDict, closed=True):
    private_link_vpce_id: (
        "capo_firehose.types.snowflake_private_link_vpce_id.SnowflakePrivateLinkVpceId"
    )
    """<p>The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see <a href="https://docs.snowflake.com/en/user-guide/admin-security-privatelink">Amazon PrivateLink & Snowflake</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeVpcConfiguration) -> dict:
    out: dict = {}
    out["PrivateLinkVpceId"] = value["private_link_vpce_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeVpcConfiguration:
    out: SnowflakeVpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PrivateLinkVpceId") is not None:
        out["private_link_vpce_id"] = data["PrivateLinkVpceId"]
    else:
        raise DeserializationError(
            "SnowflakeVpcConfiguration.private_link_vpce_id required"
        )
    return out
