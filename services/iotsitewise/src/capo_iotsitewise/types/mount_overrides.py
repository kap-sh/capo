"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_mounts_map


class MountOverrides(TypedDict, closed=True):
    compute_nodes: "capo_iotsitewise.types.compute_node_mounts_map.ComputeNodeMountsMap"
    """<p>The mount overrides for each compute node, keyed by compute node name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MountOverrides) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.compute_node_mounts_map

    out["computeNodes"] = capo_iotsitewise.types.compute_node_mounts_map.serialize_json(
        value["compute_nodes"]
    )
    return out


def deserialize_json(data: dict) -> MountOverrides:
    out: MountOverrides = {}  # type: ignore[typeddict-item]
    if data.get("computeNodes") is not None:
        import capo_iotsitewise.types.compute_node_mounts_map

        out["compute_nodes"] = (
            capo_iotsitewise.types.compute_node_mounts_map.deserialize_json(
                data["computeNodes"]
            )
        )
    else:
        out["compute_nodes"] = {}
    return out
