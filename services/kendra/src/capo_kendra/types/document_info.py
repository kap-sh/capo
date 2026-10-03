"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_list
    import capo_kendra.types.document_id


class DocumentInfo(TypedDict, closed=True):
    document_id: "capo_kendra.types.document_id.DocumentId"
    """<p>The identifier of the document.</p>"""
    attributes: NotRequired[
        "capo_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>Attributes that identify a specific version of a document to check.</p> <p>The only valid attributes are:</p> <ul> <li> <p>version</p> </li> <li> <p>datasourceId</p> </li> <li> <p>jobExecutionId</p> </li> </ul> <p>The attributes follow these rules:</p> <ul> <li> <p> <code>dataSourceId</code> and <code>jobExecutionId</code> must be used together.</p> </li> <li> <p> <code>version</code> is ignored if <code>dataSourceId</code> and <code>jobExecutionId</code> are not provided.</p> </li> <li> <p>If <code>dataSourceId</code> and <code>jobExecutionId</code> are provided, but <code>version</code> is not, the version defaults to "0".</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentInfo) -> dict:
    out: dict = {}
    out["DocumentId"] = value["document_id"]
    if "attributes" in value:
        import capo_kendra.types.document_attribute_list

        out["Attributes"] = (
            capo_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentInfo:
    out: DocumentInfo = {}  # type: ignore[typeddict-item]
    if data.get("DocumentId") is not None:
        out["document_id"] = data["DocumentId"]
    else:
        raise DeserializationError("DocumentInfo.document_id required")
    if data.get("Attributes") is not None:
        import capo_kendra.types.document_attribute_list

        out["attributes"] = (
            capo_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
