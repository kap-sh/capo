"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxChangesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.change_requests
    import capo_finspace.types.client_token_string
    import capo_finspace.types.database_name
    import capo_finspace.types.environment_id


class CreateKxChangesetRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier of the kdb environment.</p>"""
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    change_requests: "capo_finspace.types.change_requests.ChangeRequests"
    """<p>A list of change request objects that are run in order. A change request object consists of <code>changeType</code> , <code>s3Path</code>, and <code>dbPath</code>. A changeType can have the following values: </p> <ul> <li> <p>PUT – Adds or updates files in a database.</p> </li> <li> <p>DELETE – Deletes files in a database.</p> </li> </ul> <p>All the change requests require a mandatory <code>dbPath</code> attribute that defines the path within the database directory. All database paths must start with a leading / and end with a trailing /. The <code>s3Path</code> attribute defines the s3 source file path and is required for a PUT change type. The <code>s3path</code> must end with a trailing / if it is a directory and must end without a trailing / if it is a file. </p> <p>Here are few examples of how you can use the change request object:</p> <ol> <li> <p>This request adds a single sym file at database root location. </p> <p> <code>{ "changeType": "PUT", "s3Path":"s3://bucket/db/sym", "dbPath":"/"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the 2020.01.02 partition of the database.</p> <p> <code>{ "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/", "dbPath":"/2020.01.02/"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the <i>taq</i> table partition of the database.</p> <p> <code>[ { "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]</code> </p> </li> <li> <p>This request deletes the 2020.01.02 partition of the database.</p> <p> <code>[{ "changeType": "DELETE", "dbPath": "/2020.01.02/"} ]</code> </p> </li> <li> <p>The <i>DELETE</i> request allows you to delete the existing files under the 2020.01.02 partition of the database, and the <i>PUT</i> request adds a new taq table under it.</p> <p> <code>[ {"changeType": "DELETE", "dbPath":"/2020.01.02/"}, {"changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]</code> </p> </li> </ol>"""
    client_token: "capo_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxChangesetRequest) -> dict:
    out: dict = {}
    import capo_finspace.types.change_requests

    out["changeRequests"] = capo_finspace.types.change_requests.serialize_json(
        value["change_requests"]
    )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxChangesetRequest:
    out: CreateKxChangesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("changeRequests") is not None:
        import capo_finspace.types.change_requests

        out["change_requests"] = capo_finspace.types.change_requests.deserialize_json(
            data["changeRequests"]
        )
    else:
        raise DeserializationError("CreateKxChangesetRequest.change_requests required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateKxChangesetRequest.client_token required")
    return out
