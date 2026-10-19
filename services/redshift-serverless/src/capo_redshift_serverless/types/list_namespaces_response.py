"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListNamespacesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_list


class ListNamespacesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    namespaces: "capo_redshift_serverless.types.namespace_list.NamespaceList"
    """<p>The list of returned namespaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_redshift_serverless.types.namespace_list

    out["namespaces"] = (
        capo_redshift_serverless.types.namespace_list.serialize_aws_json_1_1(
            value["namespaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("namespaces") is not None:
        import capo_redshift_serverless.types.namespace_list

        out["namespaces"] = (
            capo_redshift_serverless.types.namespace_list.deserialize_aws_json_1_1(
                data["namespaces"]
            )
        )
    else:
        out["namespaces"] = []
    return out


def redact_sensitive(value: ListNamespacesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespaces" in value:
        import capo_redshift_serverless.types.namespace_list

        out["namespaces"] = (
            capo_redshift_serverless.types.namespace_list.redact_sensitive(
                value["namespaces"]
            )
        )
    return out
