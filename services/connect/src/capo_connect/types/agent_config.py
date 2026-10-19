"""Generated from Smithy shape ``com.amazonaws.connect#AgentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.distribution_list


class AgentConfig(TypedDict, closed=True):
    distributions: "capo_connect.types.distribution_list.DistributionList"
    """<p>Information about traffic distributions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentConfig) -> dict:
    out: dict = {}
    import capo_connect.types.distribution_list

    out["Distributions"] = capo_connect.types.distribution_list.serialize_json(
        value["distributions"]
    )
    return out


def deserialize_json(data: dict) -> AgentConfig:
    out: AgentConfig = {}  # type: ignore[typeddict-item]
    if data.get("Distributions") is not None:
        import capo_connect.types.distribution_list

        out["distributions"] = capo_connect.types.distribution_list.deserialize_json(
            data["Distributions"]
        )
    else:
        out["distributions"] = []
    return out
