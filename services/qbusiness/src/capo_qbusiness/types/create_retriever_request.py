"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateRetrieverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.retriever_configuration
    import capo_qbusiness.types.retriever_name
    import capo_qbusiness.types.retriever_type
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.tags


class CreateRetrieverRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of your Amazon Q Business application.</p>"""
    type: "capo_qbusiness.types.retriever_type.RetrieverType"
    """<p>The type of retriever you are using.</p>"""
    display_name: "capo_qbusiness.types.retriever_name.RetrieverName"
    """<p>The name of your retriever.</p>"""
    configuration: "capo_qbusiness.types.retriever_configuration.RetrieverConfiguration"
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business application retriever.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRetrieverRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.retriever_type

    out["type"] = capo_qbusiness.types.retriever_type.serialize_json(value["type"])
    out["displayName"] = value["display_name"]
    import capo_qbusiness.types.retriever_configuration

    out["configuration"] = capo_qbusiness.types.retriever_configuration.serialize_json(
        value["configuration"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRetrieverRequest:
    out: CreateRetrieverRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_qbusiness.types.retriever_type

        out["type"] = capo_qbusiness.types.retriever_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_qbusiness.types.retriever_type.RetrieverType", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("configuration") is not None:
        import capo_qbusiness.types.retriever_configuration

        out["configuration"] = (
            capo_qbusiness.types.retriever_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_qbusiness.types._unknown

        out["configuration"] = capo_qbusiness.types._unknown.UnknownUnionMember("")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    return out
