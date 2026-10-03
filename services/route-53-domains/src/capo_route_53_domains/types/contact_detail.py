"""Generated from Smithy shape ``com.amazonaws.route53domains#ContactDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.address_line
    import capo_route_53_domains.types.city
    import capo_route_53_domains.types.contact_name
    import capo_route_53_domains.types.contact_number
    import capo_route_53_domains.types.contact_type
    import capo_route_53_domains.types.country_code
    import capo_route_53_domains.types.email
    import capo_route_53_domains.types.extra_param_list
    import capo_route_53_domains.types.state
    import capo_route_53_domains.types.zip_code


class ContactDetail(TypedDict, closed=True):
    first_name: NotRequired["capo_route_53_domains.types.contact_name.ContactName"]
    """<p>First name of contact.</p>"""
    last_name: NotRequired["capo_route_53_domains.types.contact_name.ContactName"]
    """<p>Last name of contact.</p>"""
    contact_type: NotRequired["capo_route_53_domains.types.contact_type.ContactType"]
    """<p>Indicates whether the contact is a person, company, association, or public organization. Note the following:</p> <ul> <li> <p>If you specify a value other than <code>PERSON</code>, you must also specify a value for <code>OrganizationName</code>.</p> </li> <li> <p>For some TLDs, the privacy protection available depends on the value that you specify for <code>Contact Type</code>. For the privacy protection settings for your TLD, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i> </p> </li> <li> <p>For .es domains, the value of <code>ContactType</code> must be <code>PERSON</code> for all three contacts.</p> </li> </ul>"""
    organization_name: NotRequired[
        "capo_route_53_domains.types.contact_name.ContactName"
    ]
    """<p>Name of the organization for contact types other than <code>PERSON</code>.</p>"""
    address_line1: NotRequired["capo_route_53_domains.types.address_line.AddressLine"]
    """<p>First line of the contact's address.</p>"""
    address_line2: NotRequired["capo_route_53_domains.types.address_line.AddressLine"]
    """<p>Second line of contact's address, if any.</p>"""
    city: NotRequired["capo_route_53_domains.types.city.City"]
    """<p>The city of the contact's address.</p>"""
    state: NotRequired["capo_route_53_domains.types.state.State"]
    """<p>The state or province of the contact's city.</p>"""
    country_code: NotRequired["capo_route_53_domains.types.country_code.CountryCode"]
    """<p>Code for the country of the contact's address.</p>"""
    zip_code: NotRequired["capo_route_53_domains.types.zip_code.ZipCode"]
    """<p>The zip or postal code of the contact's address.</p>"""
    phone_number: NotRequired[
        "capo_route_53_domains.types.contact_number.ContactNumber"
    ]
    """<p>The phone number of the contact.</p> <p>Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code>]". For example, a US phone number might appear as <code>"+1.1234567890"</code>.</p>"""
    email: NotRequired["capo_route_53_domains.types.email.Email"]
    """<p>Email address of the contact.</p>"""
    fax: NotRequired["capo_route_53_domains.types.contact_number.ContactNumber"]
    """<p>Fax number of the contact.</p> <p>Constraints: Phone number must be specified in the format "+[country dialing code].[number including any area code]". For example, a US phone number might appear as <code>"+1.1234567890"</code>.</p>"""
    extra_params: NotRequired[
        "capo_route_53_domains.types.extra_param_list.ExtraParamList"
    ]
    """<p>A list of name-value pairs for parameters required by certain top-level domains.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactDetail) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "contact_type" in value:
        import capo_route_53_domains.types.contact_type

        out["ContactType"] = (
            capo_route_53_domains.types.contact_type.serialize_aws_json_1_1(
                value["contact_type"]
            )
        )
    if "organization_name" in value:
        out["OrganizationName"] = value["organization_name"]
    if "address_line1" in value:
        out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "city" in value:
        out["City"] = value["city"]
    if "state" in value:
        out["State"] = value["state"]
    if "country_code" in value:
        import capo_route_53_domains.types.country_code

        out["CountryCode"] = (
            capo_route_53_domains.types.country_code.serialize_aws_json_1_1(
                value["country_code"]
            )
        )
    if "zip_code" in value:
        out["ZipCode"] = value["zip_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "email" in value:
        out["Email"] = value["email"]
    if "fax" in value:
        out["Fax"] = value["fax"]
    if "extra_params" in value:
        import capo_route_53_domains.types.extra_param_list

        out["ExtraParams"] = (
            capo_route_53_domains.types.extra_param_list.serialize_aws_json_1_1(
                value["extra_params"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactDetail:
    out: ContactDetail = {}  # type: ignore[typeddict-item]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("ContactType") is not None:
        import capo_route_53_domains.types.contact_type

        out["contact_type"] = (
            capo_route_53_domains.types.contact_type.deserialize_aws_json_1_1(
                data["ContactType"]
            )
        )
    if data.get("OrganizationName") is not None:
        out["organization_name"] = data["OrganizationName"]
    if data.get("AddressLine1") is not None:
        out["address_line1"] = data["AddressLine1"]
    if data.get("AddressLine2") is not None:
        out["address_line2"] = data["AddressLine2"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("CountryCode") is not None:
        import capo_route_53_domains.types.country_code

        out["country_code"] = (
            capo_route_53_domains.types.country_code.deserialize_aws_json_1_1(
                data["CountryCode"]
            )
        )
    if data.get("ZipCode") is not None:
        out["zip_code"] = data["ZipCode"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("Fax") is not None:
        out["fax"] = data["Fax"]
    if data.get("ExtraParams") is not None:
        import capo_route_53_domains.types.extra_param_list

        out["extra_params"] = (
            capo_route_53_domains.types.extra_param_list.deserialize_aws_json_1_1(
                data["ExtraParams"]
            )
        )
    return out
