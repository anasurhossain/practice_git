<!-- question1.xslt -->
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Login Report <xsl:value-of select="loginReport/@date"/></h2>
                <p><b>Device name:</b> <xsl:value-of select="loginReport/device/@name"/></p>
                
                <xsl:for-each select="loginReport/device/user">
                    <p><b>Username:</b> <xsl:value-of select="@username"/></p>
                    <p><b>Name:</b> <xsl:value-of select="name"/></p>
                    <p><b>Group:</b> <xsl:value-of select="group"/></p>
                    <p><b>Login:</b></p>
                    <ul>
                        <xsl:for-each select="login">
                            <li>
                                <xsl:value-of select="@date"/>: <xsl:value-of select="."/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
