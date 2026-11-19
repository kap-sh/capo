"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteMetricDataQueryDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.definition_id


class DeleteMetricDataQueryDefinitionInput(TypedDict, closed=True):
    id: NotRequired["capo_cloudwatch.types.definition_id.DefinitionId"]
    """<p>The ID of the metric data query definition to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMetricDataQueryDefinitionInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMetricDataQueryDefinitionInput:
    out: DeleteMetricDataQueryDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteMetricDataQueryDefinitionInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))


def deserialize_query(el: Element) -> DeleteMetricDataQueryDefinitionInput:
    out: DeleteMetricDataQueryDefinitionInput = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out
