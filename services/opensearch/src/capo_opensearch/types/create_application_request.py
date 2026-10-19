"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.application_name
    import capo_opensearch.types.client_token
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.iam_identity_center_options_input
    import capo_opensearch.types.kms_key_arn
    import capo_opensearch.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_opensearch.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    name: "capo_opensearch.types.application_name.ApplicationName"
    """<p>The unique name of the OpenSearch application. Names must be unique within an Amazon Web Services Region for each account.</p>"""
    data_sources: NotRequired["capo_opensearch.types.data_sources.DataSources"]
    """<p>The data sources to link to the OpenSearch application.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
    ]
    """<p>Configuration settings for integrating Amazon Web Services IAM Identity Center with the OpenSearch application.</p>"""
    app_configs: NotRequired["capo_opensearch.types.app_configs.AppConfigs"]
    """<p>Configuration settings for the OpenSearch application, including administrative options.</p>"""
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]
    kms_key_arn: NotRequired["capo_opensearch.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest. If provided, the application uses your customer-managed key for encryption. If omitted, the application uses an AWS-managed key. The KMS key must be in the same region as the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "data_sources" in value:
        import capo_opensearch.types.data_sources

        out["dataSources"] = capo_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "iam_identity_center_options" in value:
        import capo_opensearch.types.iam_identity_center_options_input

        out["iamIdentityCenterOptions"] = (
            capo_opensearch.types.iam_identity_center_options_input.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    if "app_configs" in value:
        import capo_opensearch.types.app_configs

        out["appConfigs"] = capo_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["tagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dataSources") is not None:
        import capo_opensearch.types.data_sources

        out["data_sources"] = capo_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if data.get("iamIdentityCenterOptions") is not None:
        import capo_opensearch.types.iam_identity_center_options_input

        out["iam_identity_center_options"] = (
            capo_opensearch.types.iam_identity_center_options_input.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    if data.get("appConfigs") is not None:
        import capo_opensearch.types.app_configs

        out["app_configs"] = capo_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if data.get("tagList") is not None:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["tagList"]
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
