"""Generated from Smithy shape ``com.amazonaws.opensearch#CutoverRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cutover_target


class CutoverRequestOptions(TypedDict, closed=True):
    target: "capo_opensearch.types.cutover_target.CutoverTarget"
    """<p>The cluster to cut over to. <code>ClonedCluster</code> makes the cloned cluster serve the domain. <code>PrimaryCluster</code> keeps the primary cluster and ends the upgrade.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CutoverRequestOptions) -> dict:
    out: dict = {}
    import capo_opensearch.types.cutover_target

    out["Target"] = capo_opensearch.types.cutover_target.serialize_json(value["target"])
    return out


def deserialize_json(data: dict) -> CutoverRequestOptions:
    out: CutoverRequestOptions = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_opensearch.types.cutover_target

        out["target"] = capo_opensearch.types.cutover_target.deserialize_json(
            data["Target"]
        )
    else:
        import typing

        out["target"] = typing.cast(
            "capo_opensearch.types.cutover_target.CutoverTarget", ""
        )
    return out
