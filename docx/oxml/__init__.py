# encoding: utf-8

"""
Initializes oxml sub-package, including registering custom element classes
corresponding to Open XML elements.
"""

from docx.oxml.shared import register_custom_element_class


class ValidationError(Exception):
    """
    Raised when invalid XML is encountered, such as on attempt to access a
    missing required child element
    """


# ===========================================================================
# custom element class mappings
# ===========================================================================

from docx.oxml.shared import CT_String

from docx.oxml.shape import (
    CT_Blip, CT_BlipFillProperties, CT_GraphicalObject,
    CT_GraphicalObjectData, CT_Inline, CT_Picture, CT_PositiveSize2D
)
register_custom_element_class('a:blip', CT_Blip)
register_custom_element_class('a:graphic', CT_GraphicalObject)
register_custom_element_class('a:graphicData', CT_GraphicalObjectData)
register_custom_element_class('pic:blipFill', CT_BlipFillProperties)
register_custom_element_class('pic:pic', CT_Picture)
register_custom_element_class('wp:extent', CT_PositiveSize2D)
register_custom_element_class('wp:inline', CT_Inline)

from docx.oxml.parts.document import CT_Body, CT_Document
register_custom_element_class('w:body', CT_Body)
register_custom_element_class('w:document', CT_Document)

from docx.oxml.table import CT_Row, CT_Tbl, CT_TblGrid, CT_TblPr, CT_Tc
register_custom_element_class('w:tbl', CT_Tbl)
register_custom_element_class('w:tblGrid', CT_TblGrid)
register_custom_element_class('w:tblPr', CT_TblPr)
register_custom_element_class('w:tblStyle', CT_String)
register_custom_element_class('w:tc', CT_Tc)
register_custom_element_class('w:tr', CT_Row)

from docx.oxml.text import CT_Br, CT_P, CT_PPr, CT_R, CT_Text
register_custom_element_class('w:br', CT_Br)
register_custom_element_class('w:p', CT_P)
register_custom_element_class('w:pPr', CT_PPr)
register_custom_element_class('w:pStyle', CT_String)
register_custom_element_class('w:r', CT_R)
register_custom_element_class('w:t', CT_Text)
