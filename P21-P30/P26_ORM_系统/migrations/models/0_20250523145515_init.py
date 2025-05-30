from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `stuent` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '<PASSWORD>',
    `sno` INT NOT NULL COMMENT '学号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_stuent_clas_42705d08` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '讲师姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `tno` INT NOT NULL COMMENT '讲师编号'
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL COMMENT '课程讲师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `stuent_course` (
    `stuent_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`stuent_id`) REFERENCES `stuent` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_stuent_cour_stuent__2280db` (`stuent_id`, `course_id`)
) CHARACTER SET utf8;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
