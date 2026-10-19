"""Generated from Smithy shape ``com.amazonaws.athena#CreateNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.database_string
    import capo_athena.types.description_string
    import capo_athena.types.idempotency_token
    import capo_athena.types.name_string
    import capo_athena.types.query_string
    import capo_athena.types.work_group_name


class CreateNamedQueryInput(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The query name.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The query description.</p>"""
    database: "capo_athena.types.database_string.DatabaseString"
    """<p>The database to which the query belongs.</p>"""
    query_string: "capo_athena.types.query_string.QueryString"
    """<p>The contents of the query with all query statements.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another <code>CreateNamedQuery</code> request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the <code>QueryString</code>, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup in which the named query is being created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamedQueryInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Database"] = value["database"]
    out["QueryString"] = value["query_string"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamedQueryInput:
    out: CreateNamedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    return out
