"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_filter_conditions


class ArchiveFilters(TypedDict, closed=True):
    include: NotRequired[
        "capo_mailmanager.types.archive_filter_conditions.ArchiveFilterConditions"
    ]
    """<p>The filter conditions for emails to include.</p>"""
    unless: NotRequired[
        "capo_mailmanager.types.archive_filter_conditions.ArchiveFilterConditions"
    ]
    """<p>The filter conditions for emails to exclude.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveFilters) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_mailmanager.types.archive_filter_conditions

        out["Include"] = (
            capo_mailmanager.types.archive_filter_conditions.serialize_aws_json_1_0(
                value["include"]
            )
        )
    if "unless" in value:
        import capo_mailmanager.types.archive_filter_conditions

        out["Unless"] = (
            capo_mailmanager.types.archive_filter_conditions.serialize_aws_json_1_0(
                value["unless"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveFilters:
    out: ArchiveFilters = {}  # type: ignore[typeddict-item]
    if data.get("Include") is not None:
        import capo_mailmanager.types.archive_filter_conditions

        out["include"] = (
            capo_mailmanager.types.archive_filter_conditions.deserialize_aws_json_1_0(
                data["Include"]
            )
        )
    if data.get("Unless") is not None:
        import capo_mailmanager.types.archive_filter_conditions

        out["unless"] = (
            capo_mailmanager.types.archive_filter_conditions.deserialize_aws_json_1_0(
                data["Unless"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveFilters) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_mailmanager.types.archive_filter_conditions

        out["Include"] = (
            capo_mailmanager.types.archive_filter_conditions.serialize_cbor(
                value["include"]
            )
        )
    if "unless" in value:
        import capo_mailmanager.types.archive_filter_conditions

        out["Unless"] = capo_mailmanager.types.archive_filter_conditions.serialize_cbor(
            value["unless"]
        )
    return out


def deserialize_cbor(data: dict) -> ArchiveFilters:
    out: ArchiveFilters = {}  # type: ignore[typeddict-item]
    if data.get("Include") is not None:
        import capo_mailmanager.types.archive_filter_conditions

        out["include"] = (
            capo_mailmanager.types.archive_filter_conditions.deserialize_cbor(
                data["Include"]
            )
        )
    if data.get("Unless") is not None:
        import capo_mailmanager.types.archive_filter_conditions

        out["unless"] = (
            capo_mailmanager.types.archive_filter_conditions.deserialize_cbor(
                data["Unless"]
            )
        )
    return out
