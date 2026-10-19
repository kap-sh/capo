"""Generated from Smithy shape ``com.amazonaws.directoryservice#UnshareTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.target_id
    import capo_directory_service.types.target_type


class UnshareTarget(TypedDict, closed=True):
    id: "capo_directory_service.types.target_id.TargetId"
    """<p>Identifier of the directory consumer account.</p>"""
    type: "capo_directory_service.types.target_type.TargetType"
    """<p>Type of identifier to be used in the <i>Id</i> field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnshareTarget) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_directory_service.types.target_type

    out["Type"] = capo_directory_service.types.target_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnshareTarget:
    out: UnshareTarget = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_directory_service.types.target_type

        out["type"] = capo_directory_service.types.target_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_directory_service.types.target_type.TargetType", ""
        )
    return out
