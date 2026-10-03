"""Generated from Smithy shape ``com.amazonaws.inspector#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.asset_attributes
    import capo_inspector.types.asset_type
    import capo_inspector.types.attribute_list
    import capo_inspector.types.bool
    import capo_inspector.types.finding_id
    import capo_inspector.types.inspector_service_attributes
    import capo_inspector.types.ioc_confidence
    import capo_inspector.types.numeric_severity
    import capo_inspector.types.numeric_version
    import capo_inspector.types.service_name
    import capo_inspector.types.severity
    import capo_inspector.types.text
    import capo_inspector.types.timestamp
    import capo_inspector.types.user_attribute_list


class Finding(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the finding.</p>"""
    schema_version: "capo_inspector.types.numeric_version.NumericVersion"
    """<p>The schema version of this data type.</p>"""
    service: NotRequired["capo_inspector.types.service_name.ServiceName"]
    """<p>The data element is set to "Inspector".</p>"""
    service_attributes: NotRequired[
        "capo_inspector.types.inspector_service_attributes.InspectorServiceAttributes"
    ]
    """<p>This data type is used in the <a>Finding</a> data type.</p>"""
    asset_type: NotRequired["capo_inspector.types.asset_type.AssetType"]
    """<p>The type of the host from which the finding is generated.</p>"""
    asset_attributes: NotRequired[
        "capo_inspector.types.asset_attributes.AssetAttributes"
    ]
    """<p>A collection of attributes of the host from which the finding is generated.</p>"""
    id: NotRequired["capo_inspector.types.finding_id.FindingId"]
    """<p>The ID of the finding.</p>"""
    title: NotRequired["capo_inspector.types.text.Text"]
    """<p>The name of the finding.</p>"""
    description: NotRequired["capo_inspector.types.text.Text"]
    """<p>The description of the finding.</p>"""
    recommendation: NotRequired["capo_inspector.types.text.Text"]
    """<p>The recommendation for the finding.</p>"""
    severity: NotRequired["capo_inspector.types.severity.Severity"]
    """<p>The finding severity. Values can be set to High, Medium, Low, and Informational.</p>"""
    numeric_severity: "capo_inspector.types.numeric_severity.NumericSeverity"
    """<p>The numeric value of the finding severity.</p>"""
    confidence: "capo_inspector.types.ioc_confidence.IocConfidence"
    """<p>This data element is currently not used.</p>"""
    indicator_of_compromise: NotRequired["capo_inspector.types.bool.Bool"]
    """<p>This data element is currently not used.</p>"""
    attributes: "capo_inspector.types.attribute_list.AttributeList"
    """<p>The system-defined attributes for the finding.</p>"""
    user_attributes: "capo_inspector.types.user_attribute_list.UserAttributeList"
    """<p>The user-defined attributes that are assigned to the finding.</p>"""
    created_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time when the finding was generated.</p>"""
    updated_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time when <a>AddAttributesToFindings</a> is called.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Finding) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["schemaVersion"] = value.get("schema_version", 0)
    if "service" in value:
        out["service"] = value["service"]
    if "service_attributes" in value:
        import capo_inspector.types.inspector_service_attributes

        out["serviceAttributes"] = (
            capo_inspector.types.inspector_service_attributes.serialize_aws_json_1_1(
                value["service_attributes"]
            )
        )
    if "asset_type" in value:
        import capo_inspector.types.asset_type

        out["assetType"] = capo_inspector.types.asset_type.serialize_aws_json_1_1(
            value["asset_type"]
        )
    if "asset_attributes" in value:
        import capo_inspector.types.asset_attributes

        out["assetAttributes"] = (
            capo_inspector.types.asset_attributes.serialize_aws_json_1_1(
                value["asset_attributes"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "recommendation" in value:
        out["recommendation"] = value["recommendation"]
    if "severity" in value:
        import capo_inspector.types.severity

        out["severity"] = capo_inspector.types.severity.serialize_aws_json_1_1(
            value["severity"]
        )
    out["numericSeverity"] = (
        "NaN"
        if value.get("numeric_severity", 0) != value.get("numeric_severity", 0)
        else "Infinity"
        if value.get("numeric_severity", 0) == float("inf")
        else "-Infinity"
        if value.get("numeric_severity", 0) == float("-inf")
        else value.get("numeric_severity", 0)
    )
    out["confidence"] = value.get("confidence", 0)
    if "indicator_of_compromise" in value:
        out["indicatorOfCompromise"] = value["indicator_of_compromise"]
    import capo_inspector.types.attribute_list

    out["attributes"] = capo_inspector.types.attribute_list.serialize_aws_json_1_1(
        value["attributes"]
    )
    import capo_inspector.types.user_attribute_list

    out["userAttributes"] = (
        capo_inspector.types.user_attribute_list.serialize_aws_json_1_1(
            value["user_attributes"]
        )
    )
    import capo_inspector.types.timestamp

    out["createdAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    import capo_inspector.types.timestamp

    out["updatedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Finding.arn required")
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = 0
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("serviceAttributes") is not None:
        import capo_inspector.types.inspector_service_attributes

        out["service_attributes"] = (
            capo_inspector.types.inspector_service_attributes.deserialize_aws_json_1_1(
                data["serviceAttributes"]
            )
        )
    if data.get("assetType") is not None:
        import capo_inspector.types.asset_type

        out["asset_type"] = capo_inspector.types.asset_type.deserialize_aws_json_1_1(
            data["assetType"]
        )
    if data.get("assetAttributes") is not None:
        import capo_inspector.types.asset_attributes

        out["asset_attributes"] = (
            capo_inspector.types.asset_attributes.deserialize_aws_json_1_1(
                data["assetAttributes"]
            )
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    if data.get("severity") is not None:
        import capo_inspector.types.severity

        out["severity"] = capo_inspector.types.severity.deserialize_aws_json_1_1(
            data["severity"]
        )
    if data.get("numericSeverity") is not None:
        out["numeric_severity"] = float(data["numericSeverity"])
    else:
        out["numeric_severity"] = 0
    if data.get("confidence") is not None:
        out["confidence"] = data["confidence"]
    else:
        out["confidence"] = 0
    if data.get("indicatorOfCompromise") is not None:
        out["indicator_of_compromise"] = data["indicatorOfCompromise"]
    if data.get("attributes") is not None:
        import capo_inspector.types.attribute_list

        out["attributes"] = (
            capo_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError("Finding.attributes required")
    if data.get("userAttributes") is not None:
        import capo_inspector.types.user_attribute_list

        out["user_attributes"] = (
            capo_inspector.types.user_attribute_list.deserialize_aws_json_1_1(
                data["userAttributes"]
            )
        )
    else:
        raise DeserializationError("Finding.user_attributes required")
    if data.get("createdAt") is not None:
        import capo_inspector.types.timestamp

        out["created_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Finding.created_at required")
    if data.get("updatedAt") is not None:
        import capo_inspector.types.timestamp

        out["updated_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Finding.updated_at required")
    return out
