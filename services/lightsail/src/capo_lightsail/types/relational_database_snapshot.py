"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class RelationalDatabaseSnapshot(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the database snapshot.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the database snapshot.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the database snapshot was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The Region name and Availability Zone where the database snapshot is located.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    engine: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The software of the database snapshot (for example, <code>MySQL</code>)</p>"""
    engine_version: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The database engine version for the database snapshot (for example, <code>5.7.23</code>).</p>"""
    size_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB (for example, <code>32</code>) for the database snapshot.</p>"""
    state: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The state of the database snapshot.</p>"""
    from_relational_database_name: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the source database from which the database snapshot was created.</p>"""
    from_relational_database_arn: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the database from which the database snapshot was created.</p>"""
    from_relational_database_bundle_id: NotRequired[
        "capo_lightsail.types.string.string"
    ]
    """<p>The bundle ID of the database from which the database snapshot was created.</p>"""
    from_relational_database_blueprint_id: NotRequired[
        "capo_lightsail.types.string.string"
    ]
    """<p>The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseSnapshot) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    if "state" in value:
        out["state"] = value["state"]
    if "from_relational_database_name" in value:
        out["fromRelationalDatabaseName"] = value["from_relational_database_name"]
    if "from_relational_database_arn" in value:
        out["fromRelationalDatabaseArn"] = value["from_relational_database_arn"]
    if "from_relational_database_bundle_id" in value:
        out["fromRelationalDatabaseBundleId"] = value[
            "from_relational_database_bundle_id"
        ]
    if "from_relational_database_blueprint_id" in value:
        out["fromRelationalDatabaseBlueprintId"] = value[
            "from_relational_database_blueprint_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseSnapshot:
    out: RelationalDatabaseSnapshot = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("engine") is not None:
        out["engine"] = data["engine"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = data["sizeInGb"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("fromRelationalDatabaseName") is not None:
        out["from_relational_database_name"] = data["fromRelationalDatabaseName"]
    if data.get("fromRelationalDatabaseArn") is not None:
        out["from_relational_database_arn"] = data["fromRelationalDatabaseArn"]
    if data.get("fromRelationalDatabaseBundleId") is not None:
        out["from_relational_database_bundle_id"] = data[
            "fromRelationalDatabaseBundleId"
        ]
    if data.get("fromRelationalDatabaseBlueprintId") is not None:
        out["from_relational_database_blueprint_id"] = data[
            "fromRelationalDatabaseBlueprintId"
        ]
    return out
