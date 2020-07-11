// the header struct was shuffled a bit for CABs, which are deserialized by this in AssetStudio/SerializedFile.cpp
		public SerializedFile(AssetsManager assetsManager, string fullName, EndianBinaryReader reader)
		{
			this.assetsManager = assetsManager;
			this.reader = reader;
			this.fullName = fullName;
			this.fileName = Path.GetFileName(fullName);
			this.header = new SerializedFileHeader();
			reader.ReadUInt32();
			this.header.m_DataOffset = (long)reader.ReadUInt32();
			this.header.m_Version = reader.ReadUInt32() - 83U;
			this.header.m_MetadataSize = reader.ReadUInt32();
			this.header.m_FileSize = (long)((ulong)reader.ReadUInt32());
			if (this.header.m_Version >= 9U)
			{
				this.reader.m_Endianess = 1;
				this.m_FileEndianess = (EndianType)this.header.m_Endianess;
			}
			else
			{
				reader.Position = this.header.m_FileSize - (long)((ulong)this.header.m_MetadataSize);
				this.m_FileEndianess = (EndianType)reader.ReadByte();
			}