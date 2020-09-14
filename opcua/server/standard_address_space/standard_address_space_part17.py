
# -*- coding: utf-8 -*-
"""
DO NOT EDIT THIS FILE!
It is automatically generated from opcfoundation.org schemas. 
Date:2020-06-19 17:31:10.391761
"""
import datetime
from dateutil.tz import tzutc

from opcua import ua
from opcua.ua import NodeId, QualifiedName, NumericNodeId, StringNodeId, GuidNodeId
from opcua.ua import NodeClass, LocalizedText


def create_standard_address_space_Part17(server):
  
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23455, 0)
    node.BrowseName = QualifiedName('AliasNameType', 0)
    node.NodeClass = NodeClass.ObjectType
    node.ParentNodeId = NumericNodeId(58, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.ObjectTypeAttributes()
    attrs.DisplayName = LocalizedText("AliasNameType")
    attrs.IsAbstract = False
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(23455, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(58, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23456, 0)
    node.BrowseName = QualifiedName('AliasNameCategoryType', 0)
    node.NodeClass = NodeClass.ObjectType
    node.ParentNodeId = NumericNodeId(61, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.ObjectTypeAttributes()
    attrs.DisplayName = LocalizedText("AliasNameCategoryType")
    attrs.IsAbstract = False
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23456, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23457, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23456, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23458, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23456, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23462, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(23456, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(61, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23457, 0)
    node.BrowseName = QualifiedName('<Alias>', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23456, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    node.TypeDefinition = NumericNodeId(23455, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("<Alias>")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23457, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23455, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23457, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(11508, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23457, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23458, 0)
    node.BrowseName = QualifiedName('<SubAliasNameCategories>', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23456, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    node.TypeDefinition = NumericNodeId(23456, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("<SubAliasNameCategories>")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23458, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23459, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23458, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23458, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(11508, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23458, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23459, 0)
    node.BrowseName = QualifiedName('FindAlias', 0)
    node.NodeClass = NodeClass.Method
    node.ParentNodeId = NumericNodeId(23458, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    attrs = ua.MethodAttributes()
    attrs.DisplayName = LocalizedText("FindAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23459, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23460, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23459, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23461, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23459, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23459, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23458, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23460, 0)
    node.BrowseName = QualifiedName('InputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23459, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("InputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNameSearchPattern'
    extobj.DataType = NumericNodeId(12, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    extobj = ua.Argument()
    extobj.Name = 'ReferenceTypeFilter'
    extobj.DataType = NumericNodeId(17, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23460, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23460, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23460, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23459, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23461, 0)
    node.BrowseName = QualifiedName('OutputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23459, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("OutputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNodeList'
    extobj.DataType = NumericNodeId(23468, 0)
    extobj.ValueRank = 1
    extobj.ArrayDimensions = [0]
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23461, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23461, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23461, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23459, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23462, 0)
    node.BrowseName = QualifiedName('FindAlias', 0)
    node.NodeClass = NodeClass.Method
    node.ParentNodeId = NumericNodeId(23456, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    attrs = ua.MethodAttributes()
    attrs.DisplayName = LocalizedText("FindAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23462, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23463, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23462, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23464, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23462, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23462, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23463, 0)
    node.BrowseName = QualifiedName('InputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23462, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("InputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNameSearchPattern'
    extobj.DataType = NumericNodeId(12, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    extobj = ua.Argument()
    extobj.Name = 'ReferenceTypeFilter'
    extobj.DataType = NumericNodeId(17, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23463, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23463, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23463, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23462, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23464, 0)
    node.BrowseName = QualifiedName('OutputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23462, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("OutputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNodeList'
    extobj.DataType = NumericNodeId(23468, 0)
    extobj.ValueRank = 1
    extobj.ArrayDimensions = [0]
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23464, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(23464, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23464, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23462, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23468, 0)
    node.BrowseName = QualifiedName('AliasNameDataType', 0)
    node.NodeClass = NodeClass.DataType
    node.ParentNodeId = NumericNodeId(22, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.DataTypeAttributes()
    attrs.DisplayName = LocalizedText("AliasNameDataType")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(23468, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(22, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23469, 0)
    node.BrowseName = QualifiedName('AliasFor', 0)
    node.NodeClass = NodeClass.ReferenceType
    node.ParentNodeId = NumericNodeId(32, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.ReferenceTypeAttributes()
    attrs.DisplayName = LocalizedText("AliasFor")
    attrs.InverseName = LocalizedText("HasAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(23469, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(32, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23470, 0)
    node.BrowseName = QualifiedName('Aliases', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(85, 0)
    node.ReferenceTypeId = NumericNodeId(35, 0)
    node.TypeDefinition = NumericNodeId(23456, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("Aliases")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23470, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23476, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(35, 0)
    ref.SourceNodeId = NumericNodeId(23470, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(85, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23470, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23476, 0)
    node.BrowseName = QualifiedName('FindAlias', 0)
    node.NodeClass = NodeClass.Method
    node.ParentNodeId = NumericNodeId(23470, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    attrs = ua.MethodAttributes()
    attrs.DisplayName = LocalizedText("FindAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23476, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23477, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23476, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23478, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23476, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23470, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23477, 0)
    node.BrowseName = QualifiedName('InputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23476, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("InputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNameSearchPattern'
    extobj.DataType = NumericNodeId(12, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    extobj = ua.Argument()
    extobj.Name = 'ReferenceTypeFilter'
    extobj.DataType = NumericNodeId(17, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23477, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23477, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23476, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23478, 0)
    node.BrowseName = QualifiedName('OutputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23476, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("OutputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNodeList'
    extobj.DataType = NumericNodeId(23468, 0)
    extobj.ValueRank = 1
    extobj.ArrayDimensions = [0]
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23478, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23478, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23476, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23479, 0)
    node.BrowseName = QualifiedName('TagVariables', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23470, 0)
    node.ReferenceTypeId = NumericNodeId(35, 0)
    node.TypeDefinition = NumericNodeId(23456, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("TagVariables")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23479, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23485, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(35, 0)
    ref.SourceNodeId = NumericNodeId(23479, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23470, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23479, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23485, 0)
    node.BrowseName = QualifiedName('FindAlias', 0)
    node.NodeClass = NodeClass.Method
    node.ParentNodeId = NumericNodeId(23479, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    attrs = ua.MethodAttributes()
    attrs.DisplayName = LocalizedText("FindAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23485, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23486, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23485, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23487, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23485, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23479, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23486, 0)
    node.BrowseName = QualifiedName('InputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23485, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("InputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNameSearchPattern'
    extobj.DataType = NumericNodeId(12, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    extobj = ua.Argument()
    extobj.Name = 'ReferenceTypeFilter'
    extobj.DataType = NumericNodeId(17, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23486, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23486, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23485, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23487, 0)
    node.BrowseName = QualifiedName('OutputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23485, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("OutputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNodeList'
    extobj.DataType = NumericNodeId(23468, 0)
    extobj.ValueRank = 1
    extobj.ArrayDimensions = [0]
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23487, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23487, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23485, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23488, 0)
    node.BrowseName = QualifiedName('Topics', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23470, 0)
    node.ReferenceTypeId = NumericNodeId(35, 0)
    node.TypeDefinition = NumericNodeId(23456, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("Topics")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23488, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23494, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(35, 0)
    ref.SourceNodeId = NumericNodeId(23488, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23470, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23488, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23456, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23494, 0)
    node.BrowseName = QualifiedName('FindAlias', 0)
    node.NodeClass = NodeClass.Method
    node.ParentNodeId = NumericNodeId(23488, 0)
    node.ReferenceTypeId = NumericNodeId(47, 0)
    attrs = ua.MethodAttributes()
    attrs.DisplayName = LocalizedText("FindAlias")
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23494, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23495, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23494, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23496, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(47, 0)
    ref.SourceNodeId = NumericNodeId(23494, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23488, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23495, 0)
    node.BrowseName = QualifiedName('InputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23494, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("InputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNameSearchPattern'
    extobj.DataType = NumericNodeId(12, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    extobj = ua.Argument()
    extobj.Name = 'ReferenceTypeFilter'
    extobj.DataType = NumericNodeId(17, 0)
    extobj.ValueRank = -1
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23495, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23495, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23494, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23496, 0)
    node.BrowseName = QualifiedName('OutputArguments', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(23494, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("OutputArguments")
    attrs.DataType = NumericNodeId(296, 0)
    value = []
    extobj = ua.Argument()
    extobj.Name = 'AliasNodeList'
    extobj.DataType = NumericNodeId(23468, 0)
    extobj.ValueRank = 1
    extobj.ArrayDimensions = [0]
    value.append(extobj)
    attrs.Value = ua.Variant(value, ua.VariantType.ExtensionObject)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23496, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(23496, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23494, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23499, 0)
    node.BrowseName = QualifiedName('Default Binary', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23468, 0)
    node.ReferenceTypeId = NumericNodeId(38, 0)
    node.TypeDefinition = NumericNodeId(76, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("Default Binary")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(38, 0)
    ref.SourceNodeId = NumericNodeId(23499, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23468, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(39, 0)
    ref.SourceNodeId = NumericNodeId(23499, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23502, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23499, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(76, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23505, 0)
    node.BrowseName = QualifiedName('Default XML', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23468, 0)
    node.ReferenceTypeId = NumericNodeId(38, 0)
    node.TypeDefinition = NumericNodeId(76, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("Default XML")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(38, 0)
    ref.SourceNodeId = NumericNodeId(23505, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23468, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(39, 0)
    ref.SourceNodeId = NumericNodeId(23505, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23508, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23505, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(76, 0)
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(23511, 0)
    node.BrowseName = QualifiedName('Default JSON', 0)
    node.NodeClass = NodeClass.Object
    node.ParentNodeId = NumericNodeId(23468, 0)
    node.ReferenceTypeId = NumericNodeId(38, 0)
    node.TypeDefinition = NumericNodeId(76, 0)
    attrs = ua.ObjectAttributes()
    attrs.DisplayName = LocalizedText("Default JSON")
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(38, 0)
    ref.SourceNodeId = NumericNodeId(23511, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(23468, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(23511, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(76, 0)
    refs.append(ref)
    server.add_references(refs)
