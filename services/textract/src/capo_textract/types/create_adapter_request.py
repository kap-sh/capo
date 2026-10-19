"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_description
    import capo_textract.types.adapter_name
    import capo_textract.types.auto_update
    import capo_textract.types.client_request_token
    import capo_textract.types.feature_types
    import capo_textract.types.tag_map


class CreateAdapterRequest(TypedDict, closed=True):
    adapter_name: "capo_textract.types.adapter_name.AdapterName"
    """<p>The name to be assigned to the adapter being created.</p>"""
    client_request_token: NotRequired[
        "capo_textract.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapter requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>"""
    description: NotRequired[
        "capo_textract.types.adapter_description.AdapterDescription"
    ]
    """<p>The description to be assigned to the adapter being created.</p>"""
    feature_types: "capo_textract.types.feature_types.FeatureTypes"
    """<p>The type of feature that the adapter is being trained on. Currrenly, supported feature types are: <code>QUERIES</code> </p>"""
    auto_update: NotRequired["capo_textract.types.auto_update.AutoUpdate"]
    """<p>Controls whether or not the adapter should automatically update.</p>"""
    tags: NotRequired["capo_textract.types.tag_map.TagMap"]
    """<p>A list of tags to be added to the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterRequest) -> dict:
    out: dict = {}
    out["AdapterName"] = value["adapter_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_textract.types.feature_types

    out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
        value["feature_types"]
    )
    if "auto_update" in value:
        import capo_textract.types.auto_update

        out["AutoUpdate"] = capo_textract.types.auto_update.serialize_aws_json_1_1(
            value["auto_update"]
        )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterRequest:
    out: CreateAdapterRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdapterName") is not None:
        out["adapter_name"] = data["AdapterName"]
    else:
        out["adapter_name"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    else:
        out["feature_types"] = []
    if data.get("AutoUpdate") is not None:
        import capo_textract.types.auto_update

        out["auto_update"] = capo_textract.types.auto_update.deserialize_aws_json_1_1(
            data["AutoUpdate"]
        )
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out
