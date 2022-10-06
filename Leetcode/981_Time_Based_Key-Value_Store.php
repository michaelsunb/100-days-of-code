<?php
class TimeMap {
    public $store = array();

    function __construct() {}
  
    /**
     * @param String $key
     * @param String $value
     * @param Integer $timestamp
     * @return NULL
     */
    function set($key, $value, $timestamp) {
        if(array_key_exists($key, $this->store) == false) {
            $this->store[$key] = array();
        }
        array_push($this->store[$key], array($value, $timestamp));
    }
  
    /**
     * @param String $key
     * @param Integer $timestamp
     * @return String
     */
    function get($key, $timestamp) {
        $result = "";
        $values = $this->store[$key];
        if(array_key_exists($key, $this->store) == false) {
            $values = array();
        }
        $left = 0;
        $right = count($values) - 1;
        while ($left <= $right) {
            $mid = floor(($left + $right) / 2);
            if ($values[$mid][1] == $timestamp) {
                return $values[$mid][0];
            }
            if ($values[$mid][1] <= $timestamp) {
                $result = $values[$mid][0];
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return $result;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * $obj = TimeMap();
 * $obj->set($key, $value, $timestamp);
 * $ret_2 = $obj->get($key, $timestamp);
 */
$timeMap = new TimeMap();
$timeMap->set("foo", "bar", 1);
echo $timeMap->get("foo", 1);
echo "\n";
echo $timeMap->get("foo", 3);
echo "\n";
$timeMap->set("foo", "bar2", 4);
echo $timeMap->get("foo", 4);
echo "\n";
echo $timeMap->get("foo", 5);