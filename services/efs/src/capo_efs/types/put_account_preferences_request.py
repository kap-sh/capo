"""Generated from Smithy shape ``com.amazonaws.efs#PutAccountPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.resource_id_type


class PutAccountPreferencesRequest(TypedDict, closed=True):
    resource_id_type: "capo_efs.types.resource_id_type.ResourceIdType"
    """<p>Specifies the EFS resource ID preference to set for the user's Amazon Web Services account, in the current Amazon Web Services Region, either <code>LONG_ID</code> (17 characters), or <code>SHORT_ID</code> (8 characters).</p> <note> <p>Starting in October, 2021, you will receive an error when setting the account preference to <code>SHORT_ID</code>. Contact Amazon Web Services support if you receive an error and must use short IDs for file system and mount target resources.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPreferencesRequest) -> dict:
    out: dict = {}
    import capo_efs.types.resource_id_type

    out["ResourceIdType"] = capo_efs.types.resource_id_type.serialize_json(
        value["resource_id_type"]
    )
    return out


def deserialize_json(data: dict) -> PutAccountPreferencesRequest:
    out: PutAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceIdType") is not None:
        import capo_efs.types.resource_id_type

        out["resource_id_type"] = capo_efs.types.resource_id_type.deserialize_json(
            data["ResourceIdType"]
        )
    else:
        import typing

        out["resource_id_type"] = typing.cast(
            "capo_efs.types.resource_id_type.ResourceIdType", ""
        )
    return out
