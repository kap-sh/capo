"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CutoverOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.cutover_status
    import capo_elasticsearch_service.types.cutover_target


class CutoverOptions(TypedDict, closed=True):
    target: "capo_elasticsearch_service.types.cutover_target.CutoverTarget"
    """<p>The cluster that the domain is cutting over to.</p>"""
    status: "capo_elasticsearch_service.types.cutover_status.CutoverStatus"
    """<p>The status of the cutover.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CutoverOptions) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.cutover_target

    out["Target"] = capo_elasticsearch_service.types.cutover_target.serialize_json(
        value["target"]
    )
    import capo_elasticsearch_service.types.cutover_status

    out["Status"] = capo_elasticsearch_service.types.cutover_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CutoverOptions:
    out: CutoverOptions = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_elasticsearch_service.types.cutover_target

        out["target"] = (
            capo_elasticsearch_service.types.cutover_target.deserialize_json(
                data["Target"]
            )
        )
    else:
        import typing

        out["target"] = typing.cast(
            "capo_elasticsearch_service.types.cutover_target.CutoverTarget", ""
        )
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.cutover_status

        out["status"] = (
            capo_elasticsearch_service.types.cutover_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elasticsearch_service.types.cutover_status.CutoverStatus", ""
        )
    return out
