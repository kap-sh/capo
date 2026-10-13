"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InputChannel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.iam_role_arn
    import capo_cleanroomsml.types.input_channel_data_source


class InputChannel(TypedDict, closed=True):
    data_source: (
        "capo_cleanroomsml.types.input_channel_data_source.InputChannelDataSource"
    )
    """<p>The data source that is used to create the ML input channel.</p>"""
    role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the role used to run the query specified in the <code>dataSource</code> field of the input channel.</p> <p>Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an <code>AccessDeniedException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputChannel) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.input_channel_data_source

    out["dataSource"] = (
        capo_cleanroomsml.types.input_channel_data_source.serialize_json(
            value["data_source"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> InputChannel:
    out: InputChannel = {}  # type: ignore[typeddict-item]
    if data.get("dataSource") is not None:
        import capo_cleanroomsml.types.input_channel_data_source

        out["data_source"] = (
            capo_cleanroomsml.types.input_channel_data_source.deserialize_json(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError("InputChannel.data_source required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("InputChannel.role_arn required")
    return out


def redact_sensitive(value: InputChannel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_source" in value:
        import capo_cleanroomsml.types.input_channel_data_source

        out["data_source"] = (
            capo_cleanroomsml.types.input_channel_data_source.redact_sensitive(
                value["data_source"]
            )
        )
    return out
