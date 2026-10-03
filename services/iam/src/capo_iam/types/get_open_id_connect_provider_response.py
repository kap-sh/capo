"""Generated from Smithy shape ``com.amazonaws.iam#GetOpenIDConnectProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.client_id_list_type
    import capo_iam.types.date_type
    import capo_iam.types.open_id_connect_provider_url_type
    import capo_iam.types.tag_list_type
    import capo_iam.types.thumbprint_list_type


class GetOpenIDConnectProviderResponse(TypedDict, closed=True):
    url: NotRequired[
        "capo_iam.types.open_id_connect_provider_url_type.OpenIDConnectProviderUrlType"
    ]
    """<p>The URL that the IAM OIDC provider resource object is associated with. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html">CreateOpenIDConnectProvider</a>.</p>"""
    client_id_list: NotRequired["capo_iam.types.client_id_list_type.clientIDListType"]
    """<p>A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html">CreateOpenIDConnectProvider</a>.</p>"""
    thumbprint_list: NotRequired[
        "capo_iam.types.thumbprint_list_type.thumbprintListType"
    ]
    """<p>A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html">CreateOpenIDConnectProvider</a>. </p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time when the IAM OIDC provider resource object was created in the Amazon Web Services account.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOpenIDConnectProviderResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "url" in value:
        pairs.append((f"{key_prefix}Url", str(value["url"])))
    if "client_id_list" in value:
        import capo_iam.types.client_id_list_type

        capo_iam.types.client_id_list_type.serialize_query(
            value["client_id_list"], pairs, f"{key_prefix}ClientIDList"
        )
    if "thumbprint_list" in value:
        import capo_iam.types.thumbprint_list_type

        capo_iam.types.thumbprint_list_type.serialize_query(
            value["thumbprint_list"], pairs, f"{key_prefix}ThumbprintList"
        )
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> GetOpenIDConnectProviderResponse:
    out: GetOpenIDConnectProviderResponse = {}  # type: ignore[typeddict-item]
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_client_id_list = el.find("ClientIDList")
    if child_client_id_list is not None:
        import capo_iam.types.client_id_list_type

        out["client_id_list"] = capo_iam.types.client_id_list_type.deserialize_query(
            child_client_id_list
        )
    child_thumbprint_list = el.find("ThumbprintList")
    if child_thumbprint_list is not None:
        import capo_iam.types.thumbprint_list_type

        out["thumbprint_list"] = capo_iam.types.thumbprint_list_type.deserialize_query(
            child_thumbprint_list
        )
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
