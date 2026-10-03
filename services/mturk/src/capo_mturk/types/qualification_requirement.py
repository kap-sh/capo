"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.comparator
    import capo_mturk.types.hit_access_actions
    import capo_mturk.types.integer_list
    import capo_mturk.types.locale_list
    import capo_mturk.types.string


class QualificationRequirement(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.string.String"
    """<p> The ID of the Qualification type for the requirement.</p>"""
    comparator: "capo_mturk.types.comparator.Comparator"
    """<p>The kind of comparison to make against a Qualification's value. You can compare a Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user's profile, regardless of its value. </p>"""
    integer_values: NotRequired["capo_mturk.types.integer_list.IntegerList"]
    """<p> The integer value to compare against the Qualification's value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure. </p>"""
    locale_values: NotRequired["capo_mturk.types.locale_list.LocaleList"]
    """<p> The locale value to compare against the Qualification's value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure. </p>"""
    required_to_preview: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> DEPRECATED: Use the <code>ActionsGuarded</code> field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT's question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the <code>ActionsGuarded</code> field. </p>"""
    actions_guarded: NotRequired["capo_mturk.types.hit_access_actions.HITAccessActions"]
    """<p> Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It's possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the <code>RequiredToPreview</code> field. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationRequirement) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    import capo_mturk.types.comparator

    out["Comparator"] = capo_mturk.types.comparator.serialize_aws_json_1_1(
        value["comparator"]
    )
    if "integer_values" in value:
        import capo_mturk.types.integer_list

        out["IntegerValues"] = capo_mturk.types.integer_list.serialize_aws_json_1_1(
            value["integer_values"]
        )
    if "locale_values" in value:
        import capo_mturk.types.locale_list

        out["LocaleValues"] = capo_mturk.types.locale_list.serialize_aws_json_1_1(
            value["locale_values"]
        )
    if "required_to_preview" in value:
        out["RequiredToPreview"] = value["required_to_preview"]
    if "actions_guarded" in value:
        import capo_mturk.types.hit_access_actions

        out["ActionsGuarded"] = (
            capo_mturk.types.hit_access_actions.serialize_aws_json_1_1(
                value["actions_guarded"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QualificationRequirement:
    out: QualificationRequirement = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        raise DeserializationError(
            "QualificationRequirement.qualification_type_id required"
        )
    if data.get("Comparator") is not None:
        import capo_mturk.types.comparator

        out["comparator"] = capo_mturk.types.comparator.deserialize_aws_json_1_1(
            data["Comparator"]
        )
    else:
        raise DeserializationError("QualificationRequirement.comparator required")
    if data.get("IntegerValues") is not None:
        import capo_mturk.types.integer_list

        out["integer_values"] = capo_mturk.types.integer_list.deserialize_aws_json_1_1(
            data["IntegerValues"]
        )
    if data.get("LocaleValues") is not None:
        import capo_mturk.types.locale_list

        out["locale_values"] = capo_mturk.types.locale_list.deserialize_aws_json_1_1(
            data["LocaleValues"]
        )
    if data.get("RequiredToPreview") is not None:
        out["required_to_preview"] = data["RequiredToPreview"]
    if data.get("ActionsGuarded") is not None:
        import capo_mturk.types.hit_access_actions

        out["actions_guarded"] = (
            capo_mturk.types.hit_access_actions.deserialize_aws_json_1_1(
                data["ActionsGuarded"]
            )
        )
    return out
