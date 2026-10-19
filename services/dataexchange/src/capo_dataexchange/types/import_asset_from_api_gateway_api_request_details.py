"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromApiGatewayApiRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import capo_dataexchange.types.api_description
    import capo_dataexchange.types.id
    import capo_dataexchange.types.protocol_type


class ImportAssetFromApiGatewayApiRequestDetails(TypedDict, closed=True):
    api_description: NotRequired[
        "capo_dataexchange.types.api_description.ApiDescription"
    ]
    """<p>The API description. Markdown supported.</p>"""
    api_id: "capo_dataexchange.types.__string.__string"
    """<p>The API Gateway API ID.</p>"""
    api_key: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The API Gateway API key.</p>"""
    api_name: "capo_dataexchange.types.__string.__string"
    """<p>The API name.</p>"""
    api_specification_md5_hash: "capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    """<p>The Base64-encoded MD5 hash of the OpenAPI 3.0 JSON API specification file. It is used to ensure the integrity of the file.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The data set ID.</p>"""
    protocol_type: "capo_dataexchange.types.protocol_type.ProtocolType"
    """<p>The protocol type.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The revision ID.</p>"""
    stage: "capo_dataexchange.types.__string.__string"
    """<p>The API stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromApiGatewayApiRequestDetails) -> dict:
    out: dict = {}
    if "api_description" in value:
        out["ApiDescription"] = value["api_description"]
    out["ApiId"] = value["api_id"]
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    out["ApiName"] = value["api_name"]
    out["ApiSpecificationMd5Hash"] = value["api_specification_md5_hash"]
    out["DataSetId"] = value["data_set_id"]
    out["ProtocolType"] = value["protocol_type"]
    out["RevisionId"] = value["revision_id"]
    out["Stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromApiGatewayApiRequestDetails:
    out: ImportAssetFromApiGatewayApiRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("ApiDescription") is not None:
        out["api_description"] = data["ApiDescription"]
    if data.get("ApiId") is not None:
        out["api_id"] = data["ApiId"]
    else:
        out["api_id"] = ""
    if data.get("ApiKey") is not None:
        out["api_key"] = data["ApiKey"]
    if data.get("ApiName") is not None:
        out["api_name"] = data["ApiName"]
    else:
        out["api_name"] = ""
    if data.get("ApiSpecificationMd5Hash") is not None:
        out["api_specification_md5_hash"] = data["ApiSpecificationMd5Hash"]
    else:
        out["api_specification_md5_hash"] = ""
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("ProtocolType") is not None:
        out["protocol_type"] = data["ProtocolType"]
    else:
        out["protocol_type"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    if data.get("Stage") is not None:
        out["stage"] = data["Stage"]
    else:
        out["stage"] = ""
    return out
