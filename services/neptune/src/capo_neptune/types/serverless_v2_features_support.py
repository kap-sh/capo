"""Generated from Smithy shape ``com.amazonaws.neptune#ServerlessV2FeaturesSupport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.double_optional


class ServerlessV2FeaturesSupport(TypedDict, closed=True):
    min_capacity: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>Specifies the lower Neptune capacity unit (NCU) limit that a serverless platform version supports.</p>"""
    max_capacity: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>Specifies the upper Neptune capacity unit (NCU) limit that a serverless platform version supports.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2FeaturesSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}MinCapacity",
                (
                    "NaN"
                    if value["min_capacity"] != value["min_capacity"]
                    else "Infinity"
                    if value["min_capacity"] == float("inf")
                    else "-Infinity"
                    if value["min_capacity"] == float("-inf")
                    else str(value["min_capacity"])
                ),
            )
        )
    if "max_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}MaxCapacity",
                (
                    "NaN"
                    if value["max_capacity"] != value["max_capacity"]
                    else "Infinity"
                    if value["max_capacity"] == float("inf")
                    else "-Infinity"
                    if value["max_capacity"] == float("-inf")
                    else str(value["max_capacity"])
                ),
            )
        )


def deserialize_query(el: Element) -> ServerlessV2FeaturesSupport:
    out: ServerlessV2FeaturesSupport = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = float(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = float(child_max_capacity.text or "")
    return out
