"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClusteringConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.clustering_frequency_list


class ClusteringConfig(TypedDict, closed=True):
    frequencies: "capo_bedrock_agentcore_control.types.clustering_frequency_list.ClusteringFrequencyList"
    """<p>The list of frequencies at which clustering batch evaluations are triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusteringConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.clustering_frequency_list

    out["frequencies"] = (
        capo_bedrock_agentcore_control.types.clustering_frequency_list.serialize_json(
            value["frequencies"]
        )
    )
    return out


def deserialize_json(data: dict) -> ClusteringConfig:
    out: ClusteringConfig = {}  # type: ignore[typeddict-item]
    if data.get("frequencies") is not None:
        import capo_bedrock_agentcore_control.types.clustering_frequency_list

        out["frequencies"] = (
            capo_bedrock_agentcore_control.types.clustering_frequency_list.deserialize_json(
                data["frequencies"]
            )
        )
    else:
        out["frequencies"] = []
    return out
