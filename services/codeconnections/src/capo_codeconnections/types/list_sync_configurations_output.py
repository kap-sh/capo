"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListSyncConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.sharp_next_token
    import capo_codeconnections.types.sync_configuration_list


class ListSyncConfigurationsOutput(TypedDict, closed=True):
    sync_configurations: (
        "capo_codeconnections.types.sync_configuration_list.SyncConfigurationList"
    )
    """<p>The list of repository sync definitions returned by the request.</p>"""
    next_token: NotRequired[
        "capo_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSyncConfigurationsOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.sync_configuration_list

    out["SyncConfigurations"] = (
        capo_codeconnections.types.sync_configuration_list.serialize_aws_json_1_0(
            value["sync_configurations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSyncConfigurationsOutput:
    out: ListSyncConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("SyncConfigurations") is not None:
        import capo_codeconnections.types.sync_configuration_list

        out["sync_configurations"] = (
            capo_codeconnections.types.sync_configuration_list.deserialize_aws_json_1_0(
                data["SyncConfigurations"]
            )
        )
    else:
        out["sync_configurations"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
