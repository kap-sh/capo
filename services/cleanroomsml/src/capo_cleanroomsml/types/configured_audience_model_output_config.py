"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_destination
    import capo_cleanroomsml.types.iam_role_arn


class ConfiguredAudienceModelOutputConfig(TypedDict, closed=True):
    destination: "capo_cleanroomsml.types.audience_destination.AudienceDestination"
    role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that can write the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelOutputConfig) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.audience_destination

    out["destination"] = capo_cleanroomsml.types.audience_destination.serialize_json(
        value["destination"]
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelOutputConfig:
    out: ConfiguredAudienceModelOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("destination") is not None:
        import capo_cleanroomsml.types.audience_destination

        out["destination"] = (
            capo_cleanroomsml.types.audience_destination.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelOutputConfig.destination required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
