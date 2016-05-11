
# Dump of table articles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `articles`;

CREATE TABLE `articles` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `author_id` int(10) NOT NULL COMMENT 'author_id',
  `rule_id` int(10) NOT NULL COMMENT 'rule_id',
  `urlmd5` char(32) NOT NULL COMMENT 'url md5',
  `url` varchar(256) NOT NULL COMMENT 'url',
  `title` varchar(1024) DEFAULT '' COMMENT '文章标题',
  `body` text COMMENT '文章内容',
  `publish_time` date NOT NULL DEFAULT '0000-00-00' COMMENT '发布时间',
  `create_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `urlmd5` (`urlmd5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='articles';



# Dump of table author
# ------------------------------------------------------------

DROP TABLE IF EXISTS `author`;

CREATE TABLE `author` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `name` varchar(64) NOT NULL COMMENT '作者',
  `url` varchar(256) DEFAULT '' COMMENT '链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='author';



# Dump of table rules
# ------------------------------------------------------------

DROP TABLE IF EXISTS `rules`;

CREATE TABLE `rules` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `author_id` int(10) NOT NULL COMMENT 'author_id',
  `allow_domains` varchar(1024) DEFAULT '' COMMENT '允许的domain,多个以,分割',
  `start_urls` varchar(1024) NOT NULL COMMENT 'url, 多个以,分割',
  `next_page` varchar(256) DEFAULT '' COMMENT 'next_page',
  `allow_url` varchar(256) NOT NULL COMMENT '抽取文章的url',
  `extract_from` varchar(256) DEFAULT '',
  `title_xpath` varchar(128) DEFAULT '' COMMENT '标题',
  `body_xpath` varchar(128) DEFAULT '' COMMENT '文章内容',
  `publish_time_xpath` varchar(128) DEFAULT '' COMMENT '发布时间',
  `enable` tinyint(4) DEFAULT '1' COMMENT '状态：1可用，0不可用',
  `create_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='rules';


