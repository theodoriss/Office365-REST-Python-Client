from office365.runtime.paths.resource_path import ResourcePath
from office365.sharepoint.base_entity import BaseEntity


class RelatedField(BaseEntity):
    """Represents a Lookup Field that points to a given list on a Web site."""

    @property
    def field_id(self):
        """
        Gets the field id of the corresponding Lookup Field.
        :rtype: str or None
        """
        return self.properties.get("FieldId", None)

    @property
    def list_id(self):
        """
        Gets the ID of the List containing the corresponding Lookup Field.
        :rtype: str or None
        """
        return self.properties.get("ListId", None)

    @property
    def web_id(self):
        """
        Gets the ID of the Web containing the corresponding Lookup Field.
        :rtype: str or None
        """
        return self.properties.get("WebId", None)

    @property
    def relationship_delete_dehavior(self):
        """
        Gets delete behavior of the corresponding Lookup Field.
        :rtype: int or None
        """
        return self.properties.get("RelationshipDeleteBehavior", None)

    @property
    def lookup_list(self):
        """Specifies the List that the corresponding Lookup Field looks up to."""
        from office365.sharepoint.lists.list import List
        return self.properties.get("LookupList",
                                   List(self.context, ResourcePath("LookupList", self.resource_path)))

