
# Dump of table articles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `articles`;

CREATE TABLE `articles` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `urlmd5` char(32) NOT NULL COMMENT 'url md5',
  `url` varchar(256) NOT NULL COMMENT 'url',
  `title` varchar(1024) DEFAULT '' COMMENT '文章标题',
  `body` text COMMENT '文章内容',
  `author` varchar(256) DEFAULT '' COMMENT '作者',
  `publish_time` date NOT NULL DEFAULT '0000-00-00' COMMENT '发布时间',
  `create_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `urlmd5` (`urlmd5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='articles';



# Dump of table rules
# ------------------------------------------------------------

DROP TABLE IF EXISTS `rules`;

CREATE TABLE `rules` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `name` varchar(64) NOT NULL COMMENT 'spider名称',
  `allow_domains` varchar(1024) DEFAULT '' COMMENT '允许的domain,多个以,分割',
  `start_urls` varchar(1024) NOT NULL COMMENT 'url, 多个以,分割',
  `next_page` varchar(256) DEFAULT '' COMMENT 'next_page',
  `allow_url` varchar(256) NOT NULL COMMENT '抽取文章的url',
  `extract_from` varchar(256) DEFAULT '',
  `title_xpath` varchar(128) DEFAULT '' COMMENT '标题',
  `body_xpath` varchar(128) DEFAULT '' COMMENT '文章内容',
  `publish_time_xpath` varchar(128) DEFAULT '' COMMENT '发布时间',
  `author_xpath` varchar(128) DEFAULT '' COMMENT '作者',
  `enable` tinyint(4) DEFAULT '1' COMMENT '状态：1可用，0不可用',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='rules';
