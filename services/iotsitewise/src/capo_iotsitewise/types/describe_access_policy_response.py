"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.identity
    import capo_iotsitewise.types.permission
    import capo_iotsitewise.types.resource
    import capo_iotsitewise.types.timestamp


class DescribeAccessPolicyResponse(TypedDict, closed=True):
    access_policy_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    access_policy_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the access policy, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}</code> </p>"""
    access_policy_identity: "capo_iotsitewise.types.identity.Identity"
    """<p>The identity (IAM Identity Center user, IAM Identity Center group, or IAM user) to which this access policy applies.</p>"""
    access_policy_resource: "capo_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource (portal or project) to which this access policy provides access.</p>"""
    access_policy_permission: "capo_iotsitewise.types.permission.Permission"
    """<p>The access policy permission. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    access_policy_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the access policy was created, in Unix epoch time.</p>"""
    access_policy_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the access policy was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPolicyResponse) -> dict:
    out: dict = {}
    out["accessPolicyId"] = value["access_policy_id"]
    out["accessPolicyArn"] = value["access_policy_arn"]
    import capo_iotsitewise.types.identity

    out["accessPolicyIdentity"] = capo_iotsitewise.types.identity.serialize_json(
        value["access_policy_identity"]
    )
    import capo_iotsitewise.types.resource

    out["accessPolicyResource"] = capo_iotsitewise.types.resource.serialize_json(
        value["access_policy_resource"]
    )
    import capo_iotsitewise.types.permission

    out["accessPolicyPermission"] = capo_iotsitewise.types.permission.serialize_json(
        value["access_policy_permission"]
    )
    import capo_iotsitewise.types.timestamp

    out["accessPolicyCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["access_policy_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["accessPolicyLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["access_policy_last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAccessPolicyResponse:
    out: DescribeAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPolicyId") is not None:
        out["access_policy_id"] = data["accessPolicyId"]
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_id required"
        )
    if data.get("accessPolicyArn") is not None:
        out["access_policy_arn"] = data["accessPolicyArn"]
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_arn required"
        )
    if data.get("accessPolicyIdentity") is not None:
        import capo_iotsitewise.types.identity

        out["access_policy_identity"] = (
            capo_iotsitewise.types.identity.deserialize_json(
                data["accessPolicyIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_identity required"
        )
    if data.get("accessPolicyResource") is not None:
        import capo_iotsitewise.types.resource

        out["access_policy_resource"] = (
            capo_iotsitewise.types.resource.deserialize_json(
                data["accessPolicyResource"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_resource required"
        )
    if data.get("accessPolicyPermission") is not None:
        import capo_iotsitewise.types.permission

        out["access_policy_permission"] = (
            capo_iotsitewise.types.permission.deserialize_json(
                data["accessPolicyPermission"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_permission required"
        )
    if data.get("accessPolicyCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["access_policy_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["accessPolicyCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_creation_date required"
        )
    if data.get("accessPolicyLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["access_policy_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["accessPolicyLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_last_update_date required"
        )
    return out
